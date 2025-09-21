SELECT
    SUM(CASE WHEN UserID    IS NULL THEN 1 ELSE 0 END) AS UserID_nulls,
    SUM(CASE WHEN SessionID IS NULL THEN 1 ELSE 0 END) AS SessionID_nulls,
    SUM(CASE WHEN Timestamp IS NULL THEN 1 ELSE 0 END) AS Timestamp_nulls,
    SUM(CASE WHEN EventType IS NULL THEN 1 ELSE 0 END) AS EventType_nulls,
    SUM(CASE WHEN ProductID IS NULL THEN 1 ELSE 0 END) AS ProductID_nulls,
    SUM(CASE WHEN Amount    IS NULL THEN 1 ELSE 0 END) AS Amount_nulls,
    SUM(CASE WHEN Outcome   IS NULL THEN 1 ELSE 0 END) AS Outcome_nulls
FROM clickstream c ;

SELECT *
from clickstream c
limit 10;

select
	count(*) as cn
from clickstream;

select count(*)
from clickstream c
where outcome is not null;

select *, round(purchase_count*100/all_count,2) as `전환율`
from(select count(*) as all_count, sum(case when outcome = 'purchase' then 1 else 0 end) as purchase_count
from clickstream
group by userid) t

-- product 별로 전환율
-- 0으로 나누는 경우가 빈번하다.
select *, round(purchase_count/cn*100,2) as `상품별 전화율`
from (
	select productid, count(*) as cn, sum(case when outcome = 'purchase' then 1 else 0 end) as purchase_count
	from clickstream
	group by productid
	) t
	
-- 각 UserID별로 구매(Outcome='purchase')가 발생하기 직전에 수행한 EventType을 찾아내는 쿼리를 작성하세요.
with t as (
select userid,sessionid,eventtype,
	case when outcome='purchase' then lag(eventtype) over(partition by userid,sessionid order by timestamp) end as prev_event
from clickstream c)
select *
from t
where prev_event is not null;

-- 월단위 매출 구하기
select DATE_FORMAT(timestamp,'%Y-%m') as `month`, sum(amount) as total_revenue, count(*) as cn
from clickstream
where outcome = 'purchase'
group by DATE_FORMAT(timestamp,'%Y-%m')
order by 1;

WITH daily as(
select DAYNAME(timestamp) as dn, amount
from clickstream
where Outcome = 'purchase')
select dn, count(*) as cn, sum(amount), avg(case when amount is null then 0 else 1 end) as null_ratio
from daily
group by dn
order by dn;