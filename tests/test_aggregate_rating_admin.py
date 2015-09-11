from random import random
from django.contrib.admin import site
from django.test import TestCase
from model_mommy import mommy
from star_ratings.admin import AggregateRatingAdmin
from star_ratings.models import AggregateRating


class AdminAggregateRatingAdmin(TestCase):
    def test_stars_return_the_correct_html(self):
        average = 5 * random()
        max_val = 5
        rating = mommy.make(AggregateRating, average=average, max_value=max_val)

        res = AggregateRatingAdmin(AggregateRating, site).stars(rating)

        self.assertHTMLEqual(
            """<div style='position: relative;'>
                <span style='position: absolute; top: 0; left: 0; width: {}px; height: 10px; background: url(/static/star-ratings/images/admin_stars.png) 0px 10px'>&nbsp;</span>
                <span style='position: absolute; top: 0; left: 0; width: {}px; height: 10px; background: url(/static/star-ratings/images/admin_stars.png)'>&nbsp;</span>
            </div>""".format(max_val * 10, average * 10),
            res
        )

    def test_allow_tags_is_set_on_stars_method(self):
        self.assertTrue(AggregateRatingAdmin.stars.allow_tags)

    def test_short_description_is_set_on_stars_method(self):
        self.assertEqual('Rating average', AggregateRatingAdmin.stars.short_description)

    def test_list_display_contains_the_correct_columns(self):
        self.assertEqual(('__str__', 'stars'), AggregateRatingAdmin.list_display)

    def test_rating_is_registered(self):
        self.assertIsInstance(site._registry[AggregateRating], AggregateRatingAdmin)