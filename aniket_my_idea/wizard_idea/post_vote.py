from openerp.osv import fields,osv

class idea_post_vote(osv.osv_memory):
    """Post Vote For Idea"""
    _name="idea.post.vote"
    _description="Post Vote For Idea"
    _columns={
         'vote':fields.selection([('-1','Not Voted'),
             ('0','Very Bad'),                     
             ('25','Bad'),
             ('50','Normal'),
             ('75','Good'),
             ('100','Very Good')],
         'Post Vote',required=True),
         'note':fields.text('Description'),          
              }