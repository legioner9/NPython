# Copyright: 2009 MoinMoin:ChristopherDenter
# Copyright: 2011 MoinMoin:ReimarBauer
# Copyright: 2011 MoinMoin:ThomasWaldmann
# Copyright: 2012 MoinMoin:CheerXiao
# Copyright: 2023 MoinMoin project
# License: GNU GPL v2 (or any later version), see LICENSE.txt for details.

"""
MoinMoin CLI - Reduce Item Revisions

This script removes all revisions but the last one from all selected items.
"""

import click

from flask import current_app as app
from flask.cli import FlaskGroup

from whoosh.query import Every, Term, And, Regex

from moin.constants.keys import NAME, NAME_EXACT, REVID, WIKINAME, PARENTID, REV_NUMBER
from moin.app import create_app, before_wiki

from moin import log
logging = log.getLogger(__name__)


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass


@cli.command("maint-reduce-revisions",
             help="Remove all revisions but the last one from all selected items")
@click.option('--query', '-q', type=str, default='',
              help='Only perform the operation on items found by the given query.')
def ReduceRevisions(query):
    logging.info("Reduce revisions started")
    before_wiki()
    if query:
        q = And([Term(WIKINAME, app.cfg.interwikiname), Regex(NAME_EXACT, query)])
    else:
        q = Every()

    for current_rev in app.storage.search(q, limit=None):
        current_name = current_rev.meta[NAME]
        current_revid = current_rev.meta[REVID]
        print("Destroying historical revisions of {0!r}:".format(current_name))
        has_historical_revision = False
        for rev in current_rev.item.iter_revs():
            revid = rev.meta[REVID]
            if revid == current_revid:
                # fixup metadata and overwrite existing revision; modified time will be updated if changed
                changed = False
                meta = dict(rev.meta)
                if REV_NUMBER in meta and meta[REV_NUMBER] > 1 or REV_NUMBER not in meta:
                    changed = True
                    meta[REV_NUMBER] = 1
                if PARENTID in meta:
                    changed = True
                    del meta[PARENTID]
                if changed:
                    current_rev.item.store_revision(meta, current_rev.data, overwrite=True)
                    print("    (current rev meta data updated)")
                continue
            has_historical_revision = True
            name = rev.meta[NAME]
            if name == current_name:
                print("    Destroying revision {0}".format(revid))
            else:
                print("    Destroying revision {0} (named {1!r})".format(revid, name))
            current_rev.item.destroy_revision(revid)
        if not has_historical_revision:
            print("    (no historical revisions)")

    logging.info("Reduce revisions finished")
