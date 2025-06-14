import { mount } from "@vue/test-utils";
import HelloWorld from "@/components/HelloWorld.vue";

describe("HelloWorld.vue", () => {
  it("renderiza el texto esperado", () => {
    const wrapper = mount(HelloWorld, {
      props: { msg: "Hola Jest" },
    });
    expect(wrapper.text()).toMatch("Hola Jest");
  });
});
