from complectations.views.userview import (
    UserViewList,
    UserViewAdd,
    UserViewEdit,
    UserViewDelete,
    UserViewDetale,
    UserPasswordChangeView
)
from complectations.views.complectationsviews import (
    ComplectationsViewHome,
    ComplectationViewAdd,
    ComplectationViewEdit,
    ComplectationViewDelete,
)
from complectations.views.productview import (
    ProductViewList,
    ProductViewAdd,
    ProductViewEdit,
    ProductViewDelete,
    ProductViewDetale,
    ProductViewPDF,
    ProductViewXlsx,
    ProductViewListGroup
)
from complectations.views.procurementview import (
    ProcurementViewList,
    ProcurementViewPaidList,
    ProcurementViewUnpaidList,
    ProcurementViewAdd,
    ProcurementViewEdit,
    ProcurementViewDelete,
    ProcurementViewPDF,
    ProcurementViewXlsx
)
from complectations.views.providerview import (
    ProviderViewList,
    ProviderViewAdd,
    ProviderViewEdit,
    ProviderViewDelete,
)
from complectations.views.groupproductview import (
    GroupProductViewList,
    GroupProductViewAdd,
    GroupProductViewEdit,
    GroupProductViewDelete,
)
from complectations.views.receiptsview import (
    ReceiptsViewList,
    ReceiptsViewAdd,
    ReceiptsViewEdit,
    ReceiptsViewDelete,
    ReceiptsViewPDF,
    ReceiptsViewXlsx
)
from complectations.views.serviceview import (
    ServicesViewList,
    ServicesViewAdd,
    ServicesViewEdit,
    ServicesViewDelete,
    ServicesViewXlsx,
    ServicesViewPDF,
)


__all__ = (
    'UserViewList',
    'UserViewAdd',
    'UserViewEdit',
    'UserViewDelete',
    'UserPasswordChangeView',
    'UserViewDetale',

    'ComplectationsViewHome',
    'ComplectationViewAdd',
    'ComplectationViewEdit',
    'ComplectationViewDelete',

    'ProductViewList',
    'ProductViewAdd',
    'ProductViewEdit',
    'ProductViewDelete',
    'ProductViewDetale',
    'ProductViewPDF',
    'ProductViewXlsx',

    'ProductViewListGroup',
    'ProcurementViewList',
    'ProcurementViewPaidList',
    'ProcurementViewUnpaidList',
    'ProcurementViewAdd',
    'ProcurementViewEdit',
    'ProcurementViewDelete',
    'ProcurementViewPDF',
    'ProcurementViewXlsx',

    'ProviderViewList',
    'ProviderViewAdd',
    'ProviderViewEdit',
    'ProviderViewDelete',

    'GroupProductViewList',
    'GroupProductViewAdd',
    'GroupProductViewEdit',
    'GroupProductViewDelete',

    'ReceiptsViewList',
    'ReceiptsViewAdd',
    'ReceiptsViewEdit',
    'ReceiptsViewDelete',
    'ReceiptsViewPDF',
    'ReceiptsViewXlsx',

    'ServicesViewList',
    'ServicesViewAdd',
    'ServicesViewEdit',
    'ServicesViewDelete',
    'ServicesViewXlsx',
    'ServicesViewPDF',
)
