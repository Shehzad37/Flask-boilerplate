#!/usr/bin/env python3
##############
# Here We create Database (sqlite) and define our Schema
#############

from rvn import app,db,ma








class Cve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cve_id = db.Column(db.String(50))
    created = db.Column(db.String(20))
    last_modified = db.Column(db.String(20))
    description = db.Column(db.Text)
    severity = db.Column(db.String(32))
    impact = db.Column(db.Float, nullable=True)
    vector = db.Column(db.String(50))
    references = db.Column(db.Text)
    cpe = db.Column(db.Text)
    cvss = db.Column(db.Text)
    vendor = db.Column(db.Text)
    product = db.Column(db.Text)
    raw = db.Column(db.Text)
    active = db.Column(db.Integer)
    advisory_link = db.Column(db.String(200))
    list_vendors = db.Column(db.String(50))
    history = db.relationship('History', backref='history', lazy=True)


def __init__(self, cve_id, created, last_modified, description, severity, impact, vector, references, cpe, cvss,
             vendor, product, raw, active, list_vendors, advisory_link):
    self.cve_id = cve_id
    self.created = created
    self.last_modified = last_modified
    self.description = description
    self.severity = severity
    self.impact = impact
    self.vector = vector
    self.references = references
    self.cpe = cpe
    self.cvss = cvss
    self.vendor = vendor
    self.product = product
    self.raw = raw
    self.active = active
    self.advisory_link = advisory_link
    self.list_vendors = list_vendors


class ProductSchema(ma.Schema):
    class Meta:
        # fields = ('id', 'cve_id', 'created', 'last_modified', 'description','severity','impact','vector','references','cpe','cvss','vendor','product',
        #           'raw','active','advisory_link','list_vendors')
        fields = (
            'cve_id', 'list_vendors', 'last_modified', 'impact', 'description', 'vector')
        ordered = True


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20))
    cve_id = db.Column(db.Integer, db.ForeignKey('cve.id'))

    def __init__(self, date, cve_id):
        self.cve_id = cve_id
        self.date = date
