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

update 订单
set 货主名称=@h1,货主地址=@h2,货主城市=@h3,货主地区=@h4,货主邮政编码=@h5,货主国家=@h6,订购日期=@d1,发货日期=@d2
where 订单id=@dd_id

end
GO
