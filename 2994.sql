select d.name, round(sum(a.hours*150 + w.bonus*0.01*a.hours*150),1) AS salary
from doctors d join attendances a on d.id=a.id_doctor
			   join work_shifts w on a.id_work_shift=w.id
			   group by d.name order by salary desc;