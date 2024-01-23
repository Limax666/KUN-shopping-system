USE [ctask6]
GO
/****** Object:  Table [dbo].[供应商]    Script Date: 2023/5/22 15:12:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[供应商](
	[供应商id] [int] NOT NULL,
	[公司名称] [nvarchar](80) NULL,
	[联系人姓名] [nvarchar](60) NULL,
	[联系人职务] [nvarchar](60) NULL,
	[地址] [nvarchar](120) NULL,
	[城市] [nvarchar](30) NULL,
	[地区] [nvarchar](30) NULL,
	[邮政编码] [nvarchar](20) NULL,
	[国家] [nvarchar](30) NULL,
	[电话] [nvarchar](48) NULL,
	[传真] [nvarchar](48) NULL,
	[主页] [ntext] NULL,
 CONSTRAINT [PK_供应商] PRIMARY KEY CLUSTERED 
(
	[供应商id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
