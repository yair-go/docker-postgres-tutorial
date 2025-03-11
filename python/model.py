from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = "Customer"

    # id = Column("cid", Integer, autoincrement=True, primary_key=True)
    id: Mapped[int] = mapped_column(Integer(), autoincrement=True, primary_key=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(20))
    # company: Mapped[str] = mapped_column(String(80))
    # address: Mapped[str] = mapped_column(String(70))
    city: Mapped[str] = mapped_column(String(40))
    # state: Mapped[str] = mapped_column(String(40))
    # country: Mapped[str] = mapped_column(String(40))
    # postal_code: Mapped[str] = mapped_column(String(10))
    # phone: Mapped[str] = mapped_column(String(24))
    # fax: Mapped[str] = mapped_column(String(24))
    # email: Mapped[str] = mapped_column(String(60), nullable=False)
    # support_id: Mapped[int] = mapped_column(Integer())

    def __init__(self, first_name=None, last_name=None, city=None):
        # self.id = cid
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    def __repr__(self) -> str:
        return (
            # f"Customer(cid={self.cid!r}, "
            f"Customer (id={self.id!r}, "
            f"first_name={self.first_name!r}, "
            f"last_name={self.last_name!r})"
        )


class Invoice(Base):
    __tablename__ = "Invoice"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True,  autoincrement=True, nullable=False)
    customer_id: Mapped[int] = mapped_column(Integer(), ForeignKey("Customer.id"), nullable=False)
    date: Mapped[DateTime] = mapped_column(DateTime(), nullable=False)
    # billing_address: Mapped[str] = mapped_column(String(70))
    # billing_city: Mapped[str] = mapped_column(String(40))
    # billing_state: Mapped[str] = mapped_column(String(40))
    # billing_country: Mapped[str] = mapped_column(String(40))
    # billing_postal_code: Mapped[str] = mapped_column(String(10))
    # total: Mapped[int] = mapped_column(Integer())

    def __init__(self, cid=None):
        self.customer_id = cid
        self.date = datetime.now()

    def __repr__(self) -> str:
        return (
            f"Invoice(id={self.id!r}, "
            f"customer_id={self.customer_id!r}, "
            f"date={self.date!r})"
        )
