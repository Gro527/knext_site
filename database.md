# 知识抽取工具数据库结构
#### 用户：user
| 字段名 | 字段类型 | 描述 | 约束 |
| ------------ | ------------ | -------------|
| id | int(11) | 用户ID | pk |
| username | varchar(128) | 用户名 | not null/unique |
| pw_sha1 | varchar(128) | 用户密码sha1加密值 | not null |
| create_time | datetime | 创建时间 | not null |
| modify_time | datetime | 最近修改时间 | not null |
-----------------------------
#### 抽取任务：job
| 字段名 | 字段类型 | 描述 | 约束 |
| ------------ | ------------ | -------------|
| id | int(11) | 任务ID | pk |
| job_type_id | int | 任务类型id | not null/fk to job_type |
| job_name | varchar(128) | 任务名称 | not null |
| jon_owner_id | int | 任务owner id | not null/ fk to user |
| job_status | int | 任务状态：0正常/1归档/2删除 | not null |
| create_time | datetime | 创建时间 | not null |
| modify_time | datetime | 最近修改时间 | not null |
------------------------------
#### 知识三元组：knowledge
| 字段名 | 字段类型 | 描述 | 约束 |
| ------------ | ------------ | -------------|
| id | int(11) | 三元组ID | pk |
| job_id | int | 任务id | not null/fk to job |
| subject | varchar(128) | 主体 | not null |
| relation | varchar(128) | 关系 | not null |
| object | varchar(128) | 客体 | not null |
| type | int | 三元组类型：0自动抽取/1人工标注 | not null |
| is_badcase | int | 是否为badcase：0不是/1是 | not null |
| create_time | datetime | 创建时间 | not null |
| modify_time | datetime | 最近修改时间 | not null |
-----------------------------
#### 抽取任务类型：job
| 字段名 | 字段类型 | 描述 | 约束 |
| ------------ | ------------ | -------------|
| id | int(11) | 任务ID | pk |
| job_type_name | int | 任务类型id | not null |
| model_status | int | 模型状态：0正常/1不可用 | not null |
| create_time | datetime | 创建时间 | not null |
| modify_time | datetime | 最近修改时间 | not null |
