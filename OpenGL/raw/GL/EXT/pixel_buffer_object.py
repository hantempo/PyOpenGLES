'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_EXT_pixel_buffer_object'
_p.unpack_constants( """GL_PIXEL_PACK_BUFFER_EXT 0x88EB
GL_PIXEL_UNPACK_BUFFER_EXT 0x88EC
GL_PIXEL_PACK_BUFFER_BINDING_EXT 0x88ED
GL_PIXEL_UNPACK_BUFFER_BINDING_EXT 0x88EF""", globals())
glget.addGLGetConstant( GL_PIXEL_PACK_BUFFER_BINDING_EXT, (1,) )
glget.addGLGetConstant( GL_PIXEL_UNPACK_BUFFER_BINDING_EXT, (1,) )


def glInitPixelBufferObjectEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
