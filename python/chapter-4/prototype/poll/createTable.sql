USE [TSQLFundamentals2008]
GO

/****** Object:  Table [dbo].[KioskLog]    Script Date: 12/18/2015 14:15:02 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[KioskLog](
	[Location] [nvarchar](50) NOT NULL,
	[Session] [nvarchar](50) NOT NULL,
	[InsertTime] [datetime] NOT NULL,
	[PlayerID] [nvarchar](50) NULL,
	[MobileID] [nvarchar](50) NULL,
	[AckTime] [datetime] NULL,
	[DropTime] [datetime] NULL,
 CONSTRAINT [PK_KioskLog] PRIMARY KEY CLUSTERED 
(
	[Location] ASC,
	[Session] ASC
)WITH (PAD_INDEX  = OFF, STATISTICS_NORECOMPUTE  = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS  = ON, ALLOW_PAGE_LOCKS  = ON) ON [PRIMARY]
) ON [PRIMARY]

GO


