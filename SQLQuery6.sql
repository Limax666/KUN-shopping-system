USE [ctask6]
GO

/****** Object:  StoredProcedure [dbo].[purchase_1]    Script Date: 2023/5/20 18:25:39 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE procedure [dbo].[purchase_1](@dd_id int,@d1 datetime,@d2 datetime,@h1 char(10),@h2 char(50),@h3 char(10),@h4 char (10),@h5 char(10),@h6 char(10) )
as

begin

update ����
set ��������=@h1,������ַ=@h2,��������=@h3,��������=@h4,������������=@h5,��������=@h6,��������=@d1,��������=@d2
where ����id=@dd_id

end
GO
