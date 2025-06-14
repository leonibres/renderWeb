import { mount } from "@vue/test-utils";
import MyAppointments from "@/views/MyAppointments.vue";

// Bloque describe para las pruebas del componente MyAppointments
describe("MyAppointments.vue", () => {
  // Simula la función global fetch antes de todas las pruebas
  beforeAll(() => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve([]), // La respuesta simulada retorna un arreglo vacío
      })
    );
  });

  // Restaura la función fetch original después de todas las pruebas
  afterAll(() => {
    global.fetch.mockRestore && global.fetch.mockRestore();
    delete global.fetch;
  });

  // Prueba: debe mostrar un mensaje si no hay citas
  it("muestra mensaje si no hay citas", () => {
    const wrapper = mount(MyAppointments, {
      data() {
        return { appointments: [] }; // Establece appointments como un arreglo vacío
      },
    });

    // Verifica que se renderiza el mensaje de no hay citas
    expect(wrapper.text()).toContain("No tienes citas programadas");
  });
});
