
 # Adds the root directiory to the sys path
 # Allows importing any package defined in the root
import os, sys
sys.path.insert(0, os.path.dirname( __file__ ))

import webapp

if __name__ == '__main__':
    webapp.app.run()