-- 新建数仓 Schema
CREATE SCHEMA IF NOT EXISTS data_warehouse;

-- 实时事件事实表
CREATE TABLE IF NOT EXISTS data_warehouse.event_fact (
    user_id    VARCHAR(64),
    event_name VARCHAR(32),
    event_time TIMESTAMP,
    device_type VARCHAR(32)
);

-- 用户维度表
CREATE TABLE IF NOT EXISTS data_warehouse.user_dim (
    user_id    VARCHAR(64) PRIMARY KEY,
    region     VARCHAR(64),
    user_level VARCHAR(16)
);
