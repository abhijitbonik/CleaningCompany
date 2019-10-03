from app.allocation import api
from app.allocation.views import WorkerAllocation

api.add_resource(WorkerAllocation, '/worker_to_job', )