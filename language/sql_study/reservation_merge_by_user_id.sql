/*
문제 요구사항:
reservation에서 start_time과 end_time이 겹치는 예약을 user_id별로 겹치기 user_id,start_time,end_time 출력
*/

-- 묶어야될 예약들에 flag 달기
WITH ordered AS (
  SELECT *,
         CASE 
           WHEN start_time <= LAG(end_time) OVER (PARTITION BY user_id ORDER BY start_time) 
           THEN 0 ELSE 1 
         END AS new_group
  FROM reservation
),
grouped AS (
  SELECT *,
         SUM(new_group) OVER (PARTITION BY user_id ORDER BY start_time) AS group_id
  FROM ordered
)
SELECT *
FROM grouped