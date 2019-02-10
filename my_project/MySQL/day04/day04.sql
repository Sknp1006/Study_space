-- 连接查询
select acct.acct_no, acct.acct_name, customer.tel_no
from acct, customer;   -- 未作条件关联, 得到笛卡尔积
where acct.cust_no = customer.cust_no; -- 连接的条件

-- 加别名
select a.acct_no, a.acct_name, c.tel_no
from acct a, customer c;   -- 未作条件关联, 得到笛卡尔积
where a.cust_no = c.cust_no; -- 连接的条件




-- 课堂练习:
-- 使用eshop库, 完成如下操作:
-- 1.利用子查询,查询所有订单状态为"申请退货"的客户名称、电话号码
select cust_name, cust_tel from customers
where cust_id in (select distinct cust_id from orders where status = '5');

-- 2.利用连接查询， 查询"待送货"订单的信息
--   查询结果包含的字段有:
--     订单编号 下单时间 客户编号 客户电话 送货地址
select o.order_id, o.order_date, c.cust_id, c.cust_tel, c.address
from orders o
right join customers c
on o.status = '2' and o.cust_id = c.cust_id;

select o.order_id, o.order_date, c.cust_id, c.cust_tel, c.address
from orders o, customers c
where  o.status = '2' and o.cust_id = c.cust_id;
-- 3.创建eshop_admin用户,并授权:
--   1)eshop库的所有表、所有权限
--   2)允许从任意客户端登录
--   3)设置密码
grant all privileges on eshop.*
to 'eshop_admin'@'%'
identified by '123456';
-- 4.创建eshop_user用户,并授权:
--   1)eshop库中所有表的查询权限
--   2)允许从任意客户端登录
--   3)设置密码
grant select on eshop.*
to 'eshop_user'@'%'
identified by '123456';


