// build.mjs
import fs from "fs/promises";
import path from "path";
import { __dirname } from "./cjs-helper.js";

const mainFolderPath = path.resolve(__dirname, "..", "src", "PRT");
const outputFilePath = path.resolve(__dirname, "..", "src", "data.json");

async function generateData(folderPath) {
  try {
    const items = await fs.readdir(folderPath);
    const data = await Promise.all(
      items.map(async (item, index) => {
        const itemPath = path.join(folderPath, item);
        const stats = await fs.stat(itemPath);

        if (stats.isDirectory()) {
          // If the item is a directory, recursively generate data for it
          return generateData(itemPath);
        }

        const code = await fs.readFile(itemPath, "utf-8");
        const fileType = path.extname(item).substring(1);
        return {
          id: index + 1,
          category: "widgets",
          group: path.basename(item, path.extname(item)),
          type: "Button",
          name: `${path.basename(item, path.extname(item))} 1`,
          image: `https://media.giphy.com/media/3oKIPz3VFkF3kT5qwo/giphy.gif`,
          files: [
            {
              type: fileType,
              code,
            },
          ],
        };
      })
    );

    return data;
  } catch (error) {
    console.error("Error generating data:", error.message);
    return [];
  }
}

async function run() {
  const data = await generateData(mainFolderPath);
  const jsonData = JSON.stringify(data.flat(), null, 2);
  await fs.writeFile(outputFilePath, jsonData);
  console.log("Data generated successfully.");
}

run();
