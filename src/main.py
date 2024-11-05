import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from queries.core import create_all, insert_date

create_all()
insert_date()