import asyncio
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from queries.orm import insert_data_sync, insert_data_async

#create_tables()
#insert_data_sync()
asyncio.run(insert_data_async())