USE [ctask6]
GO

/****** Object:  Trigger [dbo].[to_product]    Script Date: 2023/5/20 21:00:17 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

create trigger [dbo].[to_product] on [dbo].[订单详细]
for update
as
begin

declare @pname char(20),
@pnum int

select @pname=产品id,
@pnum=数量
from inserted


update 产品
set 库存量=库存量-@pnum where 产品id=@pname

declare @new_num int
select @new_num=库存量 from 产品 where 产品id=@pname

if @new_num=0
	begin
	update 产品 set 中止='False' where 产品id=@pname
	end

end
GO

ALTER TABLE [dbo].[订单详细] ENABLE TRIGGER [to_product]
GO
