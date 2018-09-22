def validateDni(req):
    identificador = req.get('queryResult').get('parameters').get('DNI')
    nifRegex = '^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$'
    nieRegex = '^[XYZ][0-9]{7}[TRWAGMYFPDXBNJZSQVHLCKE]$'
    validNif = False
    validNie = False
    if re.search(nifRegex, identificador):
        validNif = True

    if re.search(nieRegex, identificador):
        validNie = True

    if validNif == False and validNie == False:
        salida = make_response(jsonify(
            {'fulfillmentText': 'El formato del identifidador Nif o Nie no es correcto, vuelva a introducirlo.'}))
        return salida

    return make_response(jsonify(req.get('queryResult').get('fulfillmentMessages')))


def validateTlf(req):
    tlf = req.get('queryResult').get('parameters').get('phone-number')
    tlfRegex = '^[0-9]{9}$'
    validTlf = False
    if re.search(tlfRegex, tlf):
        validTlf = True

    if validTlf == False:
        salida = make_response(jsonify({
            'fulfillmentText': 'El formato del telefono introducido no es correcto, ha de ser 999999999 , vuelva a introducirlo.'}))
        return salida

    return make_response(jsonify(req.get('queryResult').get('fulfillmentMessages')))


def validateEmail(req):
    email = req.get('queryResult').get('parameters').get('email')
    emailRegex = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    validEmail = False
    if re.search(emailRegex, email):
        validEmail = True

    if validEmail == False:
        salida = make_response(
            jsonify({'fulfillmentText': 'El formato del email introducido no es correcto, vuelva a introducirlo.'}))
        return salida

    return make_response(jsonify(req.get('queryResult').get('fulfillmentMessages')))

def validate_amount_term(req):
    amount = req.get('queryResult').get('parameters').get('Amount').get('number')
    term = req.get("queryResult").get('parameters').get('Term-days').get('number')
    validAmount = True
    validTerm = True
    if amount > 300 or amount < 50:
        validAmount = False
    if term > 60:
        validTerm = False

    if validAmount & validTerm:
        salida = make_response(jsonify(req.get('queryResult').get('fulfillmentMessages')))
    else:
        textoError = ''
        if validAmount == False:
            textoError = textoError + 'Solo podemos ofrecerte entre 50 y 300 Euros, indica otra cantidad por favor. '
        if validTerm == False:
            textoError = textoError + 'Lamentablemente no podemos ofrecerte más de 60 días. '
        salida = make_response(jsonify({'fulfillmentText': textoError}))
    return salida
