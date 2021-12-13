create index `txn_dt_src` on `account_transactions`(`txn_dt`);

select * from `account_transactions` where `txn_dt` > '2021-01-01';