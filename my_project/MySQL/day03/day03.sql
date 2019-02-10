-- customer
create table customer(
    cust_no varchar(32) not null,
    cust_name varchar(128) not null,
    tel_no varchar(32) not null 
);
insert into customer(cust_no, cust_name)
values('C0001', 'Jerry')  -- 报错,tel_no不能为空

-- 唯一约束示例
create table customer(
    cust_no varchar(32) unique,
    cust_name varchar(128) not null,
    tel_no varchar(32) not null 
);

-- 插入重复数据,违反唯一性约束
insert into customer
values('C0001', 'Jerry', '13512345678')
insert into customer
values('C0001', 'Tom', '13212345678')

-- 主键约束
create table customer(
    cust_no varchar(32) primary key,  -- 主键
    cust_name varchar(128) not null,
    tel_no varchar(32) not null 
);

insert into customer  -- 违反非空约束
values(null, 'Jerry', '13512345678')
insert into customer  -- 违反唯一约束
values('C0001', 'Tom', '13212345678')

-- 外键
create table account(
    acct_no varchar(32) primary key,
    cust_no varchar(32) not null,
    -- 在当前表的cust_no上添加外键约束
    -- 参照customer表的cust_no字段
    constraint foreign key(cust_no)
    references customer(cust_no)
);
-- 插入customer表中存在的客户
insert into account values('0001', 'C0001');  -- 参照完成性正确,可以插入
insert into account values('0002', 'C0010');  -- C0010不存在,插入报错

-- 删除被参照值,也会报错
delete from customer where cust_no = 'C0001';


-- 示例1: 创建账户交易明细表,并在交易流水号上创建唯一索引
create table acct_trans_detail(
    trans_sn varchar(32) not null,  -- 交易流水号
    trans_date datetime not null,  -- 交易时间
    acct_no varchar(32) not null,  -- 交易帐号
    trans_type int,  -- 交易类型
                     -- 存款,取款,刷卡,结息
    amt decimal(16,2) not null,  -- 交易金额
    unique(trans_sn),  -- 在trans_sn上创建唯一索引
    index(trans_date)  -- trans_date上建立普通索引 
);
-- 查看索引
show index from acct_trans_detail;
-- 插入数据
insert into acct_trans_detail
values('201801010001', now(), '322345000001', 1, 1000);
-- 查询时使用索引字段,会引用索引
select * from acct_trans_detail
where trans_sn = '201801010001';    

-- 创建索引
create index trans_date
on acct_trans_detail(trans_date)

alter table acct_trans_detail
add unique index trans_sn(trans_sn)

-- 导出
select * from acct
into outfile '/var/lib/mysql-files/acct.bak'
fields terminated by ','
lines terminated by '\n';
-- 导入
load data infile '/var/lib/mysql-files/acct.bak'
into table acct
fields terminated by ','
lines terminated by '\n';