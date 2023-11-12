#!/usr/bin/env python3

import sys

# HACK: insert an entrypoint for phoenix 6 so we can link to it
if sys.platform.startswith("darwin"):
    import robotpy_build.pkgcfg_provider
    from importlib.metadata import entry_points, EntryPoint

    def entry_points_hook(*args, **kwargs):
        ep = EntryPoint(
            name="phoenix6_workaround",
            value="phoenix5._osx_phoenix6_pkgcfg",
            group="robotpybuild",
        )

        eps = entry_points(*args, **kwargs)
        if isinstance(eps, dict):
            eps["robotpybuild"] = (ep, *eps.get("robotpybuild", tuple()))
        else:
            eps = (ep, *eps)
        return eps

    robotpy_build.pkgcfg_provider.entry_points = entry_points_hook

from robotpy_build.setup import setup

setup()
