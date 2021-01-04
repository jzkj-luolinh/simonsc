from sqlalchemy import Column, String, DECIMAL, DateTime, BIGINT, SMALLINT, INTEGER, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT, DOUBLE, TEXT
simons_csmar_tables = ['simons_csmar_balance_sheet', 'simons_csmar_income', 'simons_csmar_cash_flow']
Base = declarative_base()
metadata = Base.metadata


class simons_csmar_balance_sheet(Base):

    __tablename__ = 'simons_csmar_balance_sheet'

    A001 = Column(DOUBLE)
    A0011 = Column(DOUBLE)
    A001101 = Column(DOUBLE)
    A001107 = Column(DOUBLE)
    A001109 = Column(DOUBLE)
    A001110 = Column(DOUBLE)
    A001111 = Column(DOUBLE)
    A001112 = Column(DOUBLE)
    A001119 = Column(DOUBLE)
    A001120 = Column(DOUBLE)
    A001121 = Column(DOUBLE)
    A001123 = Column(DOUBLE)
    A001124 = Column(DOUBLE)
    A001125 = Column(DOUBLE)
    A001127 = Column(TEXT)
    A001128 = Column(TEXT)
    A0012 = Column(DOUBLE)
    A001202 = Column(DOUBLE)
    A001203 = Column(DOUBLE)
    A001204 = Column(DOUBLE)
    A001205 = Column(DOUBLE)
    A001206 = Column(DOUBLE)
    A001207 = Column(DOUBLE)
    A001211 = Column(DOUBLE)
    A001212 = Column(DOUBLE)
    A001213 = Column(DOUBLE)
    A001214 = Column(DOUBLE)
    A001215 = Column(DOUBLE)
    A001216 = Column(DOUBLE)
    A001217 = Column(DOUBLE)
    A001218 = Column(DOUBLE)
    A001219 = Column(DOUBLE)
    A001220 = Column(DOUBLE)
    A001221 = Column(DOUBLE)
    A001222 = Column(DOUBLE)
    A001223 = Column(DOUBLE)
    A001226 = Column(TEXT)
    A001227 = Column(TEXT)
    A001228 = Column(TEXT)
    A001229 = Column(TEXT)
    A002 = Column(DOUBLE)
    A0021 = Column(DOUBLE)
    A002101 = Column(DOUBLE)
    A002105 = Column(DOUBLE)
    A002107 = Column(DOUBLE)
    A002108 = Column(DOUBLE)
    A002109 = Column(DOUBLE)
    A002112 = Column(DOUBLE)
    A002113 = Column(DOUBLE)
    A002114 = Column(DOUBLE)
    A002115 = Column(DOUBLE)
    A002120 = Column(DOUBLE)
    A002125 = Column(DOUBLE)
    A002126 = Column(DOUBLE)
    A002127 = Column(DOUBLE)
    A002128 = Column(TEXT)
    A0022 = Column(DOUBLE)
    A002201 = Column(DOUBLE)
    A002203 = Column(DOUBLE)
    A002204 = Column(DOUBLE)
    A002205 = Column(DOUBLE)
    A002206 = Column(DOUBLE)
    A002207 = Column(DOUBLE)
    A002208 = Column(DOUBLE)
    A002209 = Column(DOUBLE)
    A002210 = Column(DOUBLE)
    A003 = Column(DOUBLE)
    A0031 = Column(DOUBLE)
    A003101 = Column(DOUBLE)
    A003102 = Column(DOUBLE)
    A003103 = Column(DOUBLE)
    A003105 = Column(DOUBLE)
    A003106 = Column(DOUBLE)
    A003107 = Column(DOUBLE)
    A003109 = Column(DOUBLE)
    A003110 = Column(DOUBLE)
    A003111 = Column(DOUBLE)
    A003112 = Column(DOUBLE)
    A00311210 = Column(DOUBLE)
    A00311220 = Column(DOUBLE)
    A00311230 = Column(DOUBLE)
    A0032 = Column(DOUBLE)
    A004 = Column(DOUBLE)
    A0B1103 = Column(DOUBLE)
    A0B1104 = Column(DOUBLE)
    A0B1105 = Column(DOUBLE)
    A0B1201 = Column(DOUBLE)
    A0B2102 = Column(DOUBLE)
    A0B2103 = Column(DOUBLE)
    A0B210310 = Column(DOUBLE)
    A0B210320 = Column(DOUBLE)
    A0D110110 = Column(DOUBLE)
    A0D1102 = Column(DOUBLE)
    A0D110210 = Column(DOUBLE)
    A0D1126 = Column(DOUBLE)
    A0D121810 = Column(DOUBLE)
    A0D210110 = Column(DOUBLE)
    A0D2122 = Column(DOUBLE)
    A0D2123 = Column(DOUBLE)
    A0D2202 = Column(DOUBLE)
    A0F1106 = Column(DOUBLE)
    A0F1108 = Column(DOUBLE)
    A0F1122 = Column(DOUBLE)
    A0F1224 = Column(DOUBLE)
    A0F13 = Column(DOUBLE)
    A0F2104 = Column(DOUBLE)
    A0F2106 = Column(DOUBLE)
    A0F2110 = Column(DOUBLE)
    A0F2210 = Column(DOUBLE)
    A0F23 = Column(DOUBLE)
    A0F3104 = Column(DOUBLE)
    A0F3108 = Column(DOUBLE)
    A0I1113 = Column(DOUBLE)
    A0I1114 = Column(DOUBLE)
    A0I1115 = Column(DOUBLE)
    A0I1116 = Column(DOUBLE)
    A0I111610 = Column(DOUBLE)
    A0I111620 = Column(DOUBLE)
    A0I111630 = Column(DOUBLE)
    A0I111640 = Column(DOUBLE)
    A0I1209 = Column(DOUBLE)
    A0I1210 = Column(DOUBLE)
    A0I1224 = Column(DOUBLE)
    A0I1225 = Column(DOUBLE)
    A0I2111 = Column(DOUBLE)
    A0I2116 = Column(DOUBLE)
    A0I2117 = Column(DOUBLE)
    A0I2118 = Column(DOUBLE)
    A0I2119 = Column(DOUBLE)
    A0I211910 = Column(DOUBLE)
    A0I211920 = Column(DOUBLE)
    A0I211930 = Column(DOUBLE)
    A0I211940 = Column(DOUBLE)
    A0I2121 = Column(DOUBLE)
    A0I2124 = Column(DOUBLE)
    date = Column(String(10), primary_key=True)
    ENDDATE = Column(DateTime)
    EVENTID = Column(TEXT)
    INDUSTRYMARK = Column(BIGINT)
    INSTITUTIONID = Column(DOUBLE)
    pub_date = Column(DateTime)
    REPORTTYPEID = Column(BIGINT)
    STATETYPECODE = Column(TEXT)
    SYMBOL = Column(String(10), primary_key=True)
    UPDATEID = Column(BIGINT)


class simons_csmar_income(Base):

    __tablename__ = 'simons_csmar_income'

    B001 = Column(DOUBLE)
    B0011 = Column(DOUBLE)
    B001101 = Column(DOUBLE)
    B0012 = Column(DOUBLE)
    B001201 = Column(DOUBLE)
    B001207 = Column(DOUBLE)
    B001209 = Column(DOUBLE)
    B001210 = Column(DOUBLE)
    B001211 = Column(DOUBLE)
    B00121110 = Column(TEXT)
    B00121120 = Column(TEXT)
    B001212 = Column(DOUBLE)
    B001216 = Column(TEXT)
    B0013 = Column(DOUBLE)
    B001301 = Column(DOUBLE)
    B001302 = Column(DOUBLE)
    B00130210 = Column(DOUBLE)
    B00130220 = Column(TEXT)
    B001303 = Column(DOUBLE)
    B001304 = Column(DOUBLE)
    B001305 = Column(TEXT)
    B001306 = Column(TEXT)
    B001307 = Column(TEXT)
    B001308 = Column(TEXT)
    B0014 = Column(DOUBLE)
    B00140010 = Column(DOUBLE)
    B0015 = Column(DOUBLE)
    B00150010 = Column(DOUBLE)
    B00150020 = Column(DOUBLE)
    B002 = Column(DOUBLE)
    B0021 = Column(DOUBLE)
    B0022 = Column(DOUBLE)
    B0023 = Column(DOUBLE)
    B0024 = Column(DOUBLE)
    B0025 = Column(DOUBLE)
    B0026 = Column(TEXT)
    B003 = Column(DOUBLE)
    B004 = Column(DOUBLE)
    B005 = Column(DOUBLE)
    B006 = Column(DOUBLE)
    B0061 = Column(DOUBLE)
    B0062 = Column(DOUBLE)
    B0063 = Column(TEXT)
    B0D1104 = Column(DOUBLE)
    B0D110410 = Column(DOUBLE)
    B0D110420 = Column(DOUBLE)
    B0D110430 = Column(DOUBLE)
    B0D110440 = Column(DOUBLE)
    B0D110450 = Column(DOUBLE)
    B0F1105 = Column(DOUBLE)
    B0F1208 = Column(DOUBLE)
    B0F1213 = Column(DOUBLE)
    B0I1103 = Column(DOUBLE)
    B0I110310 = Column(DOUBLE)
    B0I11031010 = Column(DOUBLE)
    B0I110320 = Column(DOUBLE)
    B0I110330 = Column(DOUBLE)
    B0I1202 = Column(DOUBLE)
    B0I1203 = Column(DOUBLE)
    B0I120310 = Column(DOUBLE)
    B0I120320 = Column(DOUBLE)
    B0I1204 = Column(DOUBLE)
    B0I120410 = Column(DOUBLE)
    B0I120420 = Column(DOUBLE)
    B0I1205 = Column(DOUBLE)
    B0I1206 = Column(DOUBLE)
    B0I1214 = Column(DOUBLE)
    B0I1215 = Column(DOUBLE)
    BBD1102 = Column(DOUBLE)
    BBD110210 = Column(DOUBLE)
    BBD110220 = Column(DOUBLE)
    date = Column(String(10), primary_key=True)
    ENDDATE = Column(DateTime)
    EVENTID = Column(TEXT)
    INDUSTRYMARK = Column(BIGINT)
    INSTITUTIONID = Column(DOUBLE)
    pub_date = Column(DateTime)
    REPORTTYPEID = Column(BIGINT)
    STARTDATE = Column(DateTime)
    STATETYPECODE = Column(TEXT)
    SYMBOL = Column(String(10), primary_key=True)
    UPDATEID = Column(BIGINT)


class simons_csmar_cash_flow(Base):

    __tablename__ = 'simons_csmar_cash_flow'

    C001 = Column(DOUBLE)
    C001001 = Column(DOUBLE)
    C001012 = Column(DOUBLE)
    C001013 = Column(DOUBLE)
    C001014 = Column(DOUBLE)
    C001020 = Column(DOUBLE)
    C001021 = Column(DOUBLE)
    C001022 = Column(DOUBLE)
    C0011 = Column(DOUBLE)
    C0012 = Column(DOUBLE)
    C002 = Column(DOUBLE)
    C002001 = Column(DOUBLE)
    C002002 = Column(DOUBLE)
    C002003 = Column(DOUBLE)
    C002004 = Column(DOUBLE)
    C002005 = Column(DOUBLE)
    C002006 = Column(DOUBLE)
    C002007 = Column(DOUBLE)
    C002009 = Column(DOUBLE)
    C002010 = Column(DOUBLE)
    C0021 = Column(DOUBLE)
    C0022 = Column(DOUBLE)
    C003 = Column(DOUBLE)
    C003002 = Column(DOUBLE)
    C003004 = Column(DOUBLE)
    C003005 = Column(DOUBLE)
    C003006 = Column(DOUBLE)
    C00300610 = Column(DOUBLE)
    C003007 = Column(DOUBLE)
    C003008 = Column(DOUBLE)
    C00300810 = Column(DOUBLE)
    C0030081010 = Column(DOUBLE)
    C00300820 = Column(DOUBLE)
    C0031 = Column(DOUBLE)
    C0032 = Column(DOUBLE)
    C004 = Column(DOUBLE)
    C005 = Column(DOUBLE)
    C006 = Column(DOUBLE)
    C007 = Column(DOUBLE)
    C008 = Column(DOUBLE)
    C0B1002 = Column(DOUBLE)
    C0B1003 = Column(DOUBLE)
    C0B1004 = Column(DOUBLE)
    C0B1015 = Column(DOUBLE)
    C0B1016 = Column(DOUBLE)
    C0D1008 = Column(DOUBLE)
    C0D1010 = Column(DOUBLE)
    C0D1011 = Column(DOUBLE)
    C0F1009 = Column(DOUBLE)
    C0F1018 = Column(DOUBLE)
    C0F1023 = Column(DOUBLE)
    C0F1024 = Column(DOUBLE)
    C0F1025 = Column(DOUBLE)
    C0F1026 = Column(DOUBLE)
    C0F1027 = Column(DOUBLE)
    C0F1028 = Column(DOUBLE)
    C0F1029 = Column(DOUBLE)
    C0F1030 = Column(DOUBLE)
    C0F1031 = Column(DOUBLE)
    C0F1032 = Column(DOUBLE)
    C0I1005 = Column(DOUBLE)
    C0I1006 = Column(DOUBLE)
    C0I1007 = Column(DOUBLE)
    C0I1017 = Column(DOUBLE)
    C0I1019 = Column(DOUBLE)
    C0I2008 = Column(DOUBLE)
    date = Column(String(10), primary_key=True)
    ENDDATE = Column(DateTime)
    EVENTID = Column(TEXT)
    INDUSTRYMARK = Column(BIGINT)
    INSTITUTIONID = Column(DOUBLE)
    pub_date = Column(DateTime)
    REPORTTYPEID = Column(BIGINT)
    STARTDATE = Column(DateTime)
    STATETYPECODE = Column(TEXT)
    SYMBOL = Column(String(10), primary_key=True)
    UPDATEID = Column(BIGINT)


simons_csmar_class_dict = {
    'simons_csmar_balance_sheet': simons_csmar_balance_sheet,
    'simons_csmar_income': simons_csmar_income,
    'simons_csmar_cash_flow': simons_csmar_cash_flow,
}
