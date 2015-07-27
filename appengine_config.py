import os
import sys

appstats_MAX_STACK = 20


# FABENGINE PKG LOADER
def _gae_pkg_loader():
    package_dir = "packages"
    package_dir_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), package_dir))

    packages = sorted(
        os.listdir(package_dir_path),
        key=lambda x: x.lower(),
        reverse=True)

    for filename in packages:
        filename = os.path.join(package_dir_path, filename)
        if filename.endswith('.whl') or os.path.isdir(filename):
            sys.path.insert(0, filename)
    sys.path.insert(0, package_dir_path)

_gae_pkg_loader()


try:
    if os.environ.get('APPLICATION_ID', '').startswith('dev~'):
        # Lets try and fix the SDK and make SSL work.
        from google.appengine.tools.devappserver2.python import sandbox
        sandbox._WHITE_LIST_C_MODULES += ['_ssl', '_socket']
        import ORIG_SOCKET as patched_socket
        sys.modules['socket'] = patched_socket
except ImportError:
    pass

