from apscheduler.schedulers.blocking import BlockingScheduler



from honey import my_mes

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(my_mes, 'interval',seconds =3)

sched.start()