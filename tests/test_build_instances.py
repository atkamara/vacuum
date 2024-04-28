"""
This module contains test functions to check if instances of the classes are created successfully.

Classes Tested:
- Formatter
- Field
- Item
- Page
"""
from vacuum import Model
from vacuum import Item
from scrapy import Selector
from dataclasses import dataclass

import pytest

def test_formatter_instance():
    # Test for Formatter class
    with pytest.raises(TypeError) :
        Model.Formatter()
    print("TypeError Raised")

def test_field_instance():
    # Test for Field class
    with pytest.raises(TypeError) :
        Model.Field()
    print("TypeError Raised")

def test_item_instance():
    # Test for Item class
    with pytest.raises(AttributeError) :
        Model.Item(None)
    print("AttributeError Raised")

def test_page_instance():
    # Test for Page class
    with pytest.raises(TypeError) :
        Model.Page()
    print("TypeError Raised")

def test_MainItem_instance():
    # Test for Page class
    html = '''<div style="grid-area: classified-4;"><a data-test-id="ad" data-qa-id="aditem_container" class="group/adcard flex h-[inherit] flex-col h-full" href="/vetements/2629181282.htm"><div class="mb-md flex items-center gap-sm"><img class="h-[2.4rem] w-[2.4rem] rounded-full" src="https://img.leboncoin.fr/api/v1/tenants/9a6387a1-6259-4f2c-a887-7e67f23dd4cb/domains/20bda58f-d650-462e-a72a-a5a7ecf2bf88/buckets/21d2b0bc-e54c-4b64-a30b-89127b18b785/images/profile/pictures/default/25a2432d-7939-55eb-8741-a2b082aded8d?rule=pp-small" alt="Vendeur particulier"><span class="line-clamp-1 overflow-hidden text-ellipsis break-all text-body-2 font-bold text-on-surface">Estelle p</span></div><div data-test-id="adcard-consumer-goods-list" class="adcard_c896bed2f relative flex h-[inherit]"><div data-test-id="image" class="adcard_1460f1edb relative before:block"><div class="adcard_c1f28d495 relative h-full"><div class=" relative box-border flex h-full items-center justify-center overflow-hidden bg-neutral-container min-h-[auto] min-w-[auto] rounded-md"><img src="https://img.leboncoin.fr/api/v1/lbcpb1/images/78/b5/ba/78b5bac0d112963a65804f2c4309ec94fc1131e5.jpg?rule=ad-image" class="_1cnjm absolute inset-none m-auto h-full w-full object-cover" alt=""><div class="bottom-md left-md absolute"><div class="flex"></div></div></div><div class="absolute left-md right-md top-md"></div></div><style>.adcard_c1f28d495 {
        position: absolute;
        inset: 0;
        height: auto;
      }</style></div><style>.adcard_1460f1edb::before { padding-bottom: 125% }</style><div class="adcard_ff20d1882 relative min-w-none flex-1 
          flex
          flex-col
          justify-between
        "><div class="flex min-w-none flex-col gap-y-sm"><div class="flex flex-row items-start gap-x-md"><div class="flex min-w-none items-center gap-x-sm"><p data-qa-id="aditem_title" data-title="true" title="2 Pulls allaitement" style="--maxLines: 2;" class="line-clamp-[--maxLines] text-ellipsis break-words text-body-1 font-bold text-on-surface transition-colors group-hover/adcard:text-main-variant line-clamp-2 break-normal">2 Pulls allaitement</p></div></div><div class="inline-flex flex-wrap items-baseline"><p class="flex flex-wrap items-center text-callout font-bold !leading-[--font-size-body-2-line-height] text-on-surface" data-test-id="price" aria-label="Prix: 12&nbsp;€"><span class="[&amp;_small-support]:text-caption [&amp;_small-support]:font-regular [&amp;_small-support]:text-support [&amp;_small]:text-caption [&amp;_small]:font-regular" data-qa-id="aditem_price"><span>12&nbsp;€</span></span></p><div class="adcard_587a82ada font-body-2 text-neutral before:mx-sm before:inline-block before:font-bold before:content-['·'] first:my-sm first:before:hidden">Bon état</div><style>.adcard_587a82ada { display: none }</style></div><div class="flex flex-wrap items-center gap-md"><span data-spark-component="tag" class="box-border inline-flex items-center justify-center gap-sm whitespace-nowrap text-caption font-bold h-sz-20 px-md rounded-full bg-support-container text-on-support-container">Livraison possible</span></div><div class="inline-flex flex-wrap items-baseline text-body-2 text-on-surface mt-md" data-test-id="ad-params-light">Taille 36 - S<span class="mx-sm inline-block font-bold text-neutral last:hidden">·</span>Kiabi<span class="mx-sm inline-block font-bold text-neutral last:hidden">·</span></div></div><div class="mt-sm flex items-end gap-sm"><p class="flex flex-wrap overflow-hidden overflow-hidden text-caption text-neutral"><span title="Calonne-sur-la-Lys 62350" class="mr-[1.2rem] last:mr-none">Calonne-sur-la-Lys 62350</span><span class="relative inline-block w-full before:absolute before:right-full before:top-none before:hidden before:w-[1.2rem] before:text-center before:font-bold before:content-['·'] tiny:w-auto tiny:before:inline-block" aria-label="Date de dépôt : hier à 20:55." title="hier à 20:55">hier à 20:55</span></p><div class="relative inline-block ml-auto"><div data-spark-component="popover-anchor"><button class="flex rounded-sm text-neutral hover:text-neutral-hovered" data-test-id="adcard_favorite_button" data-qa-id="listitem_save_ad" title="Ajouter l’annonce aux favoris"><svg viewBox="0 0 24 24" data-title="LikeOutline" fill="currentColor" stroke="none" class="fill-current text-neutral w-sz-24 h-sz-24" data-spark-component="icon" aria-hidden="true" focusable="false"><path d="m16.28,3c-1.72,0-3.24.83-4.28,2.11-1.04-1.28-2.57-2.11-4.28-2.11-3.21,0-5.72,2.85-5.72,6.24,0,2.77,1.41,4.75,1.97,5.51,1.87,2.47,4.38,4.11,6.67,5.6h.02c.25.17.49.33.73.49.32.21.73.22,1.06.02.21-.13.43-.26.63-.39h.02c2.39-1.48,5.02-3.1,6.95-5.68.64-.86,1.95-2.83,1.95-5.54,0-3.4-2.51-6.23-5.72-6.23h0Zm-8.57,2.12c1.46,0,2.76.96,3.35,2.39.16.38.52.64.93.64s.77-.25.93-.64c.6-1.44,1.9-2.39,3.36-2.39,1.99,0,3.7,1.79,3.69,4.13,0,2-.98,3.5-1.52,4.24-1.67,2.25-3.98,3.67-6.43,5.19l-.07.04-.21-.13c-2.33-1.52-4.54-2.97-6.18-5.14-.51-.67-1.54-2.18-1.54-4.2,0-2.33,1.7-4.13,3.7-4.13h0Z"></path></svg></button></div></div></div></div><style>.adcard_ff20d1882 {
      margin-left: 0;
      margin-top: var(--spacing-md);
      width: 100%;
    }</style></div><style>.adcard_c896bed2f {
          flex-direction: column;
          border-radius: 0;
          border: 0;
          padding: 0;
        }</style></a></div>'''
    mi = Item.MainItem(Selector(text=html))
    assert isinstance(mi,Item.MainItem)