from app.models import db, Worker, Vehicle, Equipment, Jobs, AssignJob
from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import jwt_required


class WorkerAllocation(Resource):
	@jwt_required
	def get(self):
		parser = reqparse.RequestParser()
		parser.add_argument('startDate', help = 'This field cannot be blank', required = True)
		parser.add_argument('endDate', help = 'This field cannot be blank', required = True)
		data = parser.parse_args()
		workers=self.get_available_workers(data['startDate'], data['endDate'])
		return jsonify(workers)

	def get_available_workers(self, startdate, enddate):
		workers=[]
		try:
			for job in AssignJob.objects(assign_from__gte=startdate, assign_till__lte=enddate, status=False):
				workers.append(job.worker.identification)
			return  workers
		except Exception:
			return {'msg': 'invalid date and time'}
			
	@jwt_required
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('startDate', help = 'This field cannot be blank', required = True)
		parser.add_argument('endDate', help = 'This field cannot be blank', required = True)
		parser.add_argument('job_id', help = 'This field cannot be blank', required = True)
		parser.add_argument('worker_ids', help = 'This field cannot be blank', required = True)

		data = parser.parse_args()
		try:
			job=Jobs.objects.get(id=data[job_id])
		except Exception:
			return {'msg': 'Job does not exist'}

		workers=Worker.obejcts(id__in=data['worker_ids'])
		assign_workers=[]
		try:
			available_workers=self.get_available_workers(data['startDate'], data['endDate'])
			for wk in workers:
				if wk.identification in available_workers:
					assign=AssignJob(worker=wk, job=job, assign_from=data['startDate'], assign_till=data['endDate'], status=True)
					assign.save()
					assign_workers.append(wk)
			job.update(assignedWorkers=assign_workers)
			return {'msg': 'workers successfully assigned.'}
		except Exception:
			return {'msg' : 'input errors'}



		
