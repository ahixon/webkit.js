#!/usr/bin/env python

# Copyright (c) 2009 Google Inc. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import sys

if __name__ == '__main__':
  use_internal_gyp = False

  try:
    import gyp
    try:
      gyp.input.ValidateTargetType (None, {'type': 'js_library'})
    except gyp.common.GypError, e:
      use_internal_gyp = True
      del sys.modules['gyp']
  except ImportError, e:
    use_internal_gyp = True
    del sys.modules['gyp']

  if use_internal_gyp:
    print "Using internal GYP"

    # clear existing import
    try:
      del sys.modules['gyp']
    except KeyError:
      pass

    # and subsequent self-referential imports
    for mod in sys.modules.keys():
      if mod.startswith('gyp.'):
        del sys.modules[mod]

    # add our copy to path
    import os.path
    sys.path.insert (0, os.path.join (os.path.join(os.path.dirname(sys.argv[0]), 'pylib')))
    print "python path now", sys.path

    # import local version
    import gyp

  sys.exit(gyp.script_main())
