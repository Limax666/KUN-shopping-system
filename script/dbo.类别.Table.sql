USE [ctask6]
GO
/****** Object:  Table [dbo].[类别]    Script Date: 2023/5/22 15:12:33 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[类别](
	[类别id] [int] NOT NULL,
	[类别名称] [nvarchar](30) NULL,
	[说明] [ntext] NULL,
	[图片] [image] NULL,
 CONSTRAINT [PK_类别] PRIMARY KEY CLUSTERED 
(
	[类别id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
