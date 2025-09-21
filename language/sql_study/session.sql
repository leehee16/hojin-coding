with group as(
    SELECT *,
        case when timediff(login_time,lag(log_out_time) over(partition by user_id order by login_time))<=5 then 0 else 1 end as session
    from login_log
),
session as(
    select *,
    sum(session) over(order by start_time) as session_id
)
select user_id,
