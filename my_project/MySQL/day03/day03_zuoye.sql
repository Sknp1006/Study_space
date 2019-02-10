-- 1.修改order表结构
--     1)在order_id列上添加主键约束
alter table ordres add primary key(order_id);
alter table orders modify order_id varchar(32) primary key;
--     2)在cust_id, order_date, products_num字段上添加非空约束
alter table orders modify cust_id varchar(32) not null;
alter table orders modify order_date datetime not null;
alter table orders change product_num products_num int not null;
--     3)在status字段上添加默认值,默认值为1
alter table orders modify status enum('1','2','3','4','5','6','9') default 1;
--     4)在order_date上添加普通索引
create index order_date on orders(order_date);
alter table orders add index order_date(order_date)
-- 2.创建客户信息表(customers),包含字段有
--     cust_id   客户编号, 字符串, 32位, 主键
--     cust_tel  客户电话, 字符串, 32位, 非空
--     cust_name 客户姓名, 字符串, 64位, 非空
--     address   送货地址, 字符串, 128位,非空
create table customers(
    cust_id varchar(32) primary key,
    cust_tel varchar(32) not null,
    cust_name varchar(64) not null,
    address varchar(128) not null
)default charset=utf8;
-- 3.为customers表添加数据, 要求每个orders表中的cust_id都有对应的信息
insert into customers 
values('C0001', '13512345678', 'Jerry', 'Beijing'),
('C0002', '13312345678', 'Tom', 'Hangzhou'),
('C0003', '13412345678', 'Duke', 'Harbin'),
('C0004', '13612345678', 'Joker', 'Hubei'),
('C0005', '13712345678', 'Faker', 'Hunan'),
('C0006', '13812345678', 'Jack', 'Shanghai'),
('C0007', '13912345678', 'Mike', 'Guangdong');
-- 4.在orders表的cust_id上创建外键约束
--   参照customers表的cust_id
alter table orders add
constraint cust_id foreign key(cust_id)
references customers(cust_id);
