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

update ����
set ��������=@d3,����ȷ������=@d4,�˻���=@d5
where ����id=@dd_id

declare @zk_id int
select @zk_id=�ۿ�����
from �������
where ����id=@dd_id


update ����
set �ۿ�id=@zk_id
where ����id=@dd_id

end
GO