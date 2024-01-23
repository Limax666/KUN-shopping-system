USE [ctask6]
GO

/****** Object:  Trigger [dbo].[to_product]    Script Date: 2023/5/20 21:00:17 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

create trigger [dbo].[to_product] on [dbo].[������ϸ]
for update
as
begin

declare @pname char(20),
@pnum int

select @pname=��Ʒid,
@pnum=����
from inserted


update ��Ʒ
set �����=�����-@pnum where ��Ʒid=@pname

declare @new_num int
select @new_num=����� from ��Ʒ where ��Ʒid=@pname

if @new_num=0
	begin
	update ��Ʒ set ��ֹ='False' where ��Ʒid=@pname
	end

end
GO

ALTER TABLE [dbo].[������ϸ] ENABLE TRIGGER [to_product]
GO
