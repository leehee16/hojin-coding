-- 회의실 예약 요청 중 시간대가 겹치지 않고, 먼저 요청된 예약이 없는 경우에만 예약을 확정하는 문제
select *,
    case when end_time >= lead(start_time,1,0) over(ORDER BY id) then 1 else 0 end as flag
from reservation