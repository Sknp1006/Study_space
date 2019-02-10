-- 1.创建一个库eshop,并指定编码为utf-8
create database eshop;
-- 2.创建订单表(order, utf-8编码),包含如下字段:
--     order_id  订单编号,字符串,32字节
--     cust_id   客户编号,字符串,32字节
--     order_date 下单时间,DateTime类型
--     status    订单状态,枚举类型,取值范围
--               ('1','2','3','4','5','6','9')
--               1-待付款   2-待发货
--               3-已发货   4-已收货
--               5-申请退货  6-以退货
--               9-已废弃
--     product_num 订单包含的商品数量
--     amt       订单金额,浮点数,两位小数
create table orders(
    order_id varchar(32),
    cust_id varchar(32),
    order_date datetime,
    status enum('1','2','3','4','5','6','9'),
    product_num int,
    amt decimal(16,2)
)default charset=utf8;
-- 3.至少插入5笔数据(要求数据库看上去尽量真实)
insert into orders values('O0002', 'C0002', now(), '1', 17, 998.01),
                        ('O0003', 'C0003', now(), '1', 104, 1184.00),
                        ('O0004', 'C0004', now(), '1', 240, 2948.50),
                        ('O0005', 'C0005', now(), '1', 900, 9665.00),
                        ('O0006', 'C0006', now(), '1', 8, 98.00),
                        ('O0007', 'C0007', now(), '2', 19, 1998.70),
                        ('O0008', 'C0001', now(), '2', 110, 1111.11),
                        ('O0009', 'C0002', now(), '2', 1000, 22222.00),
                        ('O0010', 'C0003', now(), '2', 3, 79.00),
                        ('O0011', 'C0004', now(), '3', 3, 98.00),
                        ('O0012', 'C0005', now(), '3', 3, 84.00),
                        ('O0013', 'C0006', now(), '3', 1, 10.00),
                        ('O0014', 'C0001', now(), '3', 6, 789.00),
                        ('O0015', 'C0002', now(), '4', 5, 666.00),
                        ('O0016', 'C0003', now(), '4', 1, 999.00);

-- 4.编写11个sql语句
--   1)查找所有的待付款订单
select * from orders where status = 1;
--   2)查找所有已发货、已收货、申请退货订单
select * from orders where status in('3','4','5');
--   3)查找某个客户的待发货订单
select * from orders where status = 2 and cust_id = 'C0007';
--   4)根据订单编号,查找订单下单日期,订单状态
select order_date, status from orders where order_id = 'O0002';
--   5)查找某个客户的所有订单,并按照下单时间倒序排列
select * from orders where cust_id = 'C0009' order by order_date desc;
--   6)统计每种状态的订单笔数
select status '订单状态', count(status) '订单数量' from orders group by status;
--   7)查询单笔订单的最大值/最小值/平均值,所有订单的总金额
select max(amt) from orders;
select min(amt) from orders;
select avg(amt) from orders;
select sum(amt) from orders;
select max(amt),min(amt),sum(amt),avg(amt) from orders;
--   8)查询金额最大的前3笔订单
select order_id, cust_id, amt from orders order by amt desc limit 3;
--   9)在表的最后添加两个字段:
--     invoice  开票状态,整数
alter table orders add invoice int;
--     invoice_date 开票时间,DateTime类型
alter table orders add invoice_date datetime;
--   10)修改某个订单状态为"已收货"
update orders set status = '4' where order_id = 'O0014';
--   11)删除已废弃的订单
delete from orders where status = '9';
