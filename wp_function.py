def wp_paragraph(p_text):
    code = f"<!-- wp:paragraph --><p>{p_text}</p><!-- /wp:paragraph -->"
    return code

def wp_h2(heading_text):
    code = f"<!-- wp:heading --><h2>{heading_text}</h2><!-- /wp:heading -->"
    return code

def wp_h3(heading_text):
    code = f"<!-- wp:heading --><h3>{heading_text}</h3><!-- /wp:heading -->"
    return code