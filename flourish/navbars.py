from django.conf import settings
from edc_navbar import NavbarItem, site_navbars, Navbar


flourish = Navbar(name='flourish')

flourish.append_item(
    NavbarItem(
        name='maternal_dataset',
        label='Maternal Dataset',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('maternal_dataset_listboard_url')))

flourish.append_item(
    NavbarItem(
        name='maternal_screening',
        label='Maternal Screening',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('maternal_screening_listboard_url')))

flourish.append_item(
    NavbarItem(
        name='maternal_subject',
        label='Maternal Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')))

flourish.append_item(
    NavbarItem(
        name='worklist',
        title='Worklist',
        label='Worklist',
        fa_icon='fa-user-plus',
        url_name=settings.DASHBOARD_URL_NAMES.get('flourish_follow_listboard_url')))

site_navbars.register(flourish)
