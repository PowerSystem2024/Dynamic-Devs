class Cliente extends Persona {
    // Atributo estatico
    static contadorClientes = 0;

    // Constructor
    constructor(nombre, apellido, edad, ficharegistro) {
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = this._fechaRegistro;
    }

    get idCliente() {
        return this._idCliente;
    } 

    get fechaRegistro() {
        return this._fechaRegistro;
    }

    set fechaRegistro(fechaRegistro) {
        this._fechaRegistro = fechaRegistro
    }

    toString() {
        return `
        ${super.toString()} 
        ${this._idCliente} 
        ${this._fechaRegistro}`;
    }
}    