'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_fragment_lighting'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_fragment_lighting',False)
_p.unpack_constants( """GL_FRAGMENT_LIGHTING_SGIX 0x8400
GL_FRAGMENT_COLOR_MATERIAL_SGIX 0x8401
GL_FRAGMENT_COLOR_MATERIAL_FACE_SGIX 0x8402
GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX 0x8403
GL_MAX_FRAGMENT_LIGHTS_SGIX 0x8404
GL_MAX_ACTIVE_LIGHTS_SGIX 0x8405
GL_CURRENT_RASTER_NORMAL_SGIX 0x8406
GL_LIGHT_ENV_MODE_SGIX 0x8407
GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX 0x8408
GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX 0x8409
GL_FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX 0x840A
GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX 0x840B
GL_FRAGMENT_LIGHT0_SGIX 0x840C
GL_FRAGMENT_LIGHT1_SGIX 0x840D
GL_FRAGMENT_LIGHT2_SGIX 0x840E
GL_FRAGMENT_LIGHT3_SGIX 0x840F
GL_FRAGMENT_LIGHT4_SGIX 0x8410
GL_FRAGMENT_LIGHT5_SGIX 0x8411
GL_FRAGMENT_LIGHT6_SGIX 0x8412
GL_FRAGMENT_LIGHT7_SGIX 0x8413""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum)
def glFragmentColorMaterialSGIX( face,mode ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glFragmentLightfSGIX( light,pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glFragmentLightfvSGIX( light,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glFragmentLightiSGIX( light,pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glFragmentLightivSGIX( light,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glFragmentLightModelfSGIX( pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glFragmentLightModelfvSGIX( pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glFragmentLightModeliSGIX( pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glFragmentLightModelivSGIX( pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLfloat)
def glFragmentMaterialfSGIX( face,pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glFragmentMaterialfvSGIX( face,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint)
def glFragmentMaterialiSGIX( face,pname,param ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glFragmentMaterialivSGIX( face,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetFragmentLightfvSGIX( light,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetFragmentLightivSGIX( light,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLfloatArray)
def glGetFragmentMaterialfvSGIX( face,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,arrays.GLintArray)
def glGetFragmentMaterialivSGIX( face,pname,params ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glLightEnviSGIX( pname,param ):pass


def glInitFragmentLightingSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
