from odoo import models,fields,api
from pip._internal.utils import logging


class HumanName(models.Model):

    _name = 'human.name'
    _description = 'Human name'
    _rec_name = 'text'

    use = fields.Selection(
        string="Use",
        selection=[
            ("usual", "Usual"),
            ("official", "Official"),
            ("temp", "Temp"),
            ("nickname", "Nickname"),
            ("anonymous", "Anonymous"),
            ("old", "Old"),
            ("maiden", "Maiden")],
        default="usual",
        help="The use of a human name.",
        )

    text = fields.Char(
        string="Full Name",
        help="A full text representation of the human name.",invisible=True)

    family = fields.Char(
        string="Family Name",
        help="Family name (often called 'Surname')")


    given = fields.One2many(
        "human.name.given",
        "given_name_id",
        string="Given",
        help="Given names (not always 'first'). Includes middle names",
        )



    prefix= fields.One2many(
      "human.name.prefix",
      "prefix_name_id",
        string="Prefix",
        help="Parts that come before the name."
            )

    suffix = fields.One2many(
        "human.name.suffix",
        "suffix_name_id",
        string="Suffix",
        help="Parts that come after the name",
    )

    start=fields.Date(
        string="Period:(FROM)",
        help="Time period when name was/is in use"
    )
    end = fields.Date(
        string="Period:(TO)",
        help="Time period when name was/is in use"
    )






class Given(models.Model):
    _name ="human.name.given"
    _description = 'Given'
    _rec_name = "given_name_text"

    given_name_text = fields.Char(string="Given Name",help="Given names (not always 'first'). Includes middle names")
    given_name_id=fields.Many2one("human.name",string="Given name id")


class SuffixHumanName(models.Model):
    _name = 'human.name.suffix'
    _description = "Human Name Suffix"

    suffix_name=fields.Char(string="Name")
    suffix_title=fields.Char(string="Title")
    suffix_name_id=fields.Many2one("human.name",string="Suffix id")

class PrefixHumanName(models.Model):
    _name = 'human.name.prefix'
    _description = "Human Name Prefix"

    prefix_name=fields.Char(string="Name")
    prefix_title=fields.Char(string="Title")
    prefix_name_id=fields.Many2one("human.name",string="Prefix id")



















