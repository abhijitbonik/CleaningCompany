from app.models import db, Worker, Vehicle, Equipment, Jobs, AssignJob


def get_available_workers(startdate, enddate):
	workers_assigned=[]
	for job in AssignJob.objects(assign_from__gte=startdate, assign_till__lte=enddate, status=False):
		workers_assigned.append(job.worker)
	print(workers_assigned)


		
