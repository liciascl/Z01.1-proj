-- Elementos de Sistemas
-- by Luciano Soares
-- Add16.vhd

-- Soma dois valores de 16 bits
-- ignorando o carry mais significativo

library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity Add16 is
	port(
		a   :  in STD_LOGIC_VECTOR(15 downto 0);
		b   :  in STD_LOGIC_VECTOR(15 downto 0);
		q   : out STD_LOGIC_VECTOR(15 downto 0)
	);
end entity;

architecture rtl of Add16 is
  -- Aqui declaramos sinais (fios auxiliares)
  -- e componentes (outros módulos) que serao
  -- utilizados nesse modulo.

  component FullAdder is
    port(
      a,b,c:      in STD_LOGIC;   -- entradas
      soma,vaium: out STD_LOGIC   -- sum e carry
    );
  end component;
  signal c0, c1, c2, c3: STD_LOGIC;
  signal c4, c5, c6, c7: STD_LOGIC;
  signal c8, c9, c10, c11: STD_LOGIC;
  signal c12, c13, c14, c15, c16: STD_LOGIC;
begin
  c0 <= '0';
  -- Implementação vem aqui!
  x0: FullAdder port map(a(0),b(0),c0,q(0),c1);
  x1: FullAdder port map(a(1),b(1),c1,q(1),c2);
  x2: FullAdder port map(a(2),b(2),c2,q(2),c3);
  x3: FullAdder port map(a(3),b(3),c3,q(3),c4);
  x4: FullAdder port map(a(4),b(4),c4,q(4),c5);
  x5: FullAdder port map(a(5),b(5),c5,q(5),c6);
  x6: FullAdder port map(a(6),b(6),c6,q(6),c7);
  x7: FullAdder port map(a(7),b(7),c7,q(7),c8);
  x8: FullAdder port map(a(8),b(8),c8,q(8),c9);
  x9: FullAdder port map(a(9),b(9),c9,q(9),c10);
  x10: FullAdder port map(a(10),b(10),c10,q(10),c11);
  x11: FullAdder port map(a(11),b(11),c11,q(11),c12);
  x12: FullAdder port map(a(12),b(12),c12,q(12),c13);
  x13: FullAdder port map(a(13),b(13),c13,q(13),c14);
  x14: FullAdder port map(a(14),b(14),c14,q(14),c15);
  x15: FullAdder port map(a(15),b(15),c15,q(15),c16);
end architecture;
