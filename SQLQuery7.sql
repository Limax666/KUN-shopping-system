USE [ctask6]
GO

/****** Object:  StoredProcedure [dbo].[purchase_2]    Script Date: 2023/5/20 18:25:54 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

create procedure [dbo].[purchase_2](@dd_id int,@d3 datetime,@d4 datetime,@d5 money)
as
begin

update 订单
set 到货日期=@d3,货款确认日期=@d4,运货费=@d5
where 订单id=@dd_id

declare @zk_id int
select @zk_id=折扣类型
from 订单金额
where 订单id=@dd_id


update 订单
set 折扣id=@zk_id
where 订单id=@dd_id

end
GO