Pixeland -or- Example App for issue #12165
==========================================

https://code.google.com/p/googleappengine/issues/detail?id=12165#makechanges

Preface:

Pixieland lives on the magical plane of Port 9001. But the evil dude lives on
the plane of dispair on Port 9000 (the default module).

Upload your magic to pixieland. But be warned, if the evil dude gets ahold of
your magic, he might destroy pixieland and all the unicorns. Oh no!

Installation
------------

 1. Create Virtualenv (because, you know, best practices and all that) ::

      $ mkvirtualenv pixieland

 2. Install GAE SDK into the virtualenv the only way you know how ::
 
      $ pip install git+https://github.com/xlevus/gae-setuptools.git

 3. Open a temporal portal to Pixieland and the plane-of-evil.

      $ ./open_a_portal.sh

 4. Upload the magic! ::

      $ ./upload_the_magic.sh

 5. Alternatively, open a browser to http://localhost:9001 and upload your
    magic there.

