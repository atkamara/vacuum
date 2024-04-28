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
    html = '''                      <div class="listings-cards__list-item">
                        <div
                          class="listing-card listing-card--tab listing-card--has-content listing-card--highlight-placeholder"
                        >
                          <a
                            href="https://www.test-site.com/annonce/centre-dappels-6056386"
                            class="listing-card__inner"
                            id="listing-6056386"
                            data-t-listing=""
                            data-t-listing_context="search"
                            data-t-listing_id="6056386"
                            data-t-listing_title="Centre d'Appels"
                            data-t-listing_type="classified"
                            data-t-listing_category_title="Emploi vente et commercial"
                            data-t-listing_category_slug="emploi-vente-commercial"
                            data-t-listing_slug="centre-dappels"
                            data-t-listing_price="0"
                            data-t-listing_currency=""
                            data-t-listing_location_title="Liberte 6 extension"
                            data-t-listing_source="ed_sn"
                            data-t-listing_product_slugs="listing"
                            data-uuid-ui="6056386"
                            data-ei="not-set"
                            ><div class="listing-card__aside">
                              <div class="listing-card__image">
                                <div
                                  class="listing-card__image__inner-container"
                                >
                                  <svg
                                    class="i i-jobs listing-card__image__placeholder"
                                    aria-hidden="true"
                                  >
                                    <use
                                      xlink:href="https://www.test-site.com/assets/ed-site/icons/category.48eeb376.svg#jobs"
                                    ></use>
                                  </svg>
                                  <div class="listing-card__image__inner">
                                    <img
                                      class="listing-card__image__resource vh-img"
                                      alt="Centre d'Appels"
                                      src="https://i.roamcdn.net/hz/ed/listing-thumb-224w/04b5375ca21184b4dde2027303d970a8/-/horizon-files-prod/ed/picture/qenq4ev9/73f70842ddaed70d34872e9cdcd9c424b2d87aaf.jpg"
                                      loading="lazy"
                                      srcset="
                                        https://i.roamcdn.net/hz/ed/listing-thumb-112w/e467bb1653809cd0401f719ca176f5d3/-/horizon-files-prod/ed/picture/qenq4ev9/73f70842ddaed70d34872e9cdcd9c424b2d87aaf.jpg 112w,
                                        https://i.roamcdn.net/hz/ed/listing-thumb-224w/04b5375ca21184b4dde2027303d970a8/-/horizon-files-prod/ed/picture/qenq4ev9/73f70842ddaed70d34872e9cdcd9c424b2d87aaf.jpg 224w,
                                        https://i.roamcdn.net/hz/ed/listing-thumb-180w/50c3ebea639c3be0f1725244f83571bb/-/horizon-files-prod/ed/picture/qenq4ev9/73f70842ddaed70d34872e9cdcd9c424b2d87aaf.jpg 180w,
                                        https://i.roamcdn.net/hz/ed/listing-thumb-360w/7ba6f0f262b2646cfc376b874ebc39db/-/horizon-files-prod/ed/picture/qenq4ev9/73f70842ddaed70d34872e9cdcd9c424b2d87aaf.jpg 360w
                                      "
                                    />
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="listing-card__content 1">
                              <div class="listing-card__content__inner">
                                <div class="listing-card__header">
                                  <div class="listing-card__header-content">
                                    <div class="listing-card__header__title">
                                      Centre d'Appels
                                    </div>
                                    <div
                                      class="listing-card__header__tags"
                                    ></div>
                                    <div class="listing-card__header__location">
                                      <svg class="i i-gmaps" aria-hidden="true">
                                        <use
                                          xlink:href="https://www.test-site.com/assets/ed-site/icons/map.acdc5323.svg#gmaps"
                                        ></use>
                                      </svg>
                                      Liberte 6 extension, Dakar
                                    </div>
                                  </div>
                                </div>
                                <div class="listing-card__date-line">
                                  <div class="listing-card__header__date">
                                    Hier, 10:49
                                  </div>
                                </div>
                              </div>
                            </div></a
                          >
                        </div>
                      </div>'''
    mi = Item.MainItem(Selector(text=html))
    assert isinstance(mi,Item.MainItem)