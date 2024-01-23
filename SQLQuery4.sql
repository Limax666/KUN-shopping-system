USE [ctask6]
GO
/****** Object:  StoredProcedure [dbo].[purchase]    Script Date: 2023/5/20 18:22:27 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER procedure [dbo].[purchase]
@dd_id int,
@cp_id int,
@amount int
as
begin

declare @old_num int
select @old_num=库存量 from 产品 where 产品id=@cp_id
if @old_num<@amount
	begin
	return 'failed'
	end
else
	begin
	insert 订单详细 values(@dd_id,@cp_id,@amount)
	return 'success'
	end

end
